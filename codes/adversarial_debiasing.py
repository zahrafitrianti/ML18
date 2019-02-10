from aif360.algorithms.inprocessing import AdversarialDebiasing
from sklearn.metrics import accuracy_score
from aif360.metrics import BinaryLabelDatasetMetric, ClassificationMetric
import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

# apply adversarial debiasing algorithm
def adversarial(train, test, privileged_groups, unprivileged_groups):
    sess = tf.Session()
    adversarial_model = AdversarialDebiasing(privileged_groups, unprivileged_groups, scope_name='debias_classifier', debias=True, sess=sess)
    adversarial_model.fit(train)

    # predict outcome using the test set
    pred_adversarial = adversarial_model.predict(test)
    sess.close()
    tf.reset_default_graph()

    # calculate accuracy
    accuracy = accuracy_score(y_true = test.labels, y_pred = pred_adversarial.labels)

    # calculate fairness metrics
    metric_test = BinaryLabelDatasetMetric(pred_adversarial, unprivileged_groups=unprivileged_groups, privileged_groups=privileged_groups)
    acc_test = ClassificationMetric(test, pred_adversarial, unprivileged_groups=unprivileged_groups, privileged_groups=privileged_groups)
    # metrics = [metric_test.mean_difference(), acc_test.disparate_impact(), acc_test.equal_opportunity_difference(), acc_test.average_odds_difference(), acc_test.theil_index()]
    metrics = [metric_test.mean_difference(), acc_test.disparate_impact(), acc_test.theil_index()]

    return pred_adversarial, accuracy, metrics
