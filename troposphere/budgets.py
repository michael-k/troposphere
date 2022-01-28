# Copyright (c) 2012-2022, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***


from . import AWSObject, AWSProperty, PropsDictType
from .validators import boolean, double


class CostTypes(AWSProperty):
    """
    `CostTypes <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-costtypes.html>`__
    """

    props: PropsDictType = {
        "IncludeCredit": (boolean, False),
        "IncludeDiscount": (boolean, False),
        "IncludeOtherSubscription": (boolean, False),
        "IncludeRecurring": (boolean, False),
        "IncludeRefund": (boolean, False),
        "IncludeSubscription": (boolean, False),
        "IncludeSupport": (boolean, False),
        "IncludeTax": (boolean, False),
        "IncludeUpfront": (boolean, False),
        "UseAmortized": (boolean, False),
        "UseBlended": (boolean, False),
    }


class Spend(AWSProperty):
    """
    `Spend <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-spend.html>`__
    """

    props: PropsDictType = {
        "Amount": (double, True),
        "Unit": (str, True),
    }


class TimePeriod(AWSProperty):
    """
    `TimePeriod <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-timeperiod.html>`__
    """

    props: PropsDictType = {
        "End": (str, False),
        "Start": (str, False),
    }


class BudgetData(AWSProperty):
    """
    `BudgetData <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-budgetdata.html>`__
    """

    props: PropsDictType = {
        "BudgetLimit": (Spend, False),
        "BudgetName": (str, False),
        "BudgetType": (str, True),
        "CostFilters": (dict, False),
        "CostTypes": (CostTypes, False),
        "PlannedBudgetLimits": (dict, False),
        "TimePeriod": (TimePeriod, False),
        "TimeUnit": (str, True),
    }


class Notification(AWSProperty):
    """
    `Notification <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-notification.html>`__
    """

    props: PropsDictType = {
        "ComparisonOperator": (str, True),
        "NotificationType": (str, True),
        "Threshold": (double, True),
        "ThresholdType": (str, False),
    }


class Subscriber(AWSProperty):
    """
    `Subscriber <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-subscriber.html>`__
    """

    props: PropsDictType = {
        "Address": (str, True),
        "SubscriptionType": (str, True),
    }


class NotificationWithSubscribers(AWSProperty):
    """
    `NotificationWithSubscribers <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-notificationwithsubscribers.html>`__
    """

    props: PropsDictType = {
        "Notification": (Notification, True),
        "Subscribers": ([Subscriber], True),
    }


class Budget(AWSObject):
    """
    `Budget <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-budgets-budget.html>`__
    """

    resource_type = "AWS::Budgets::Budget"

    props: PropsDictType = {
        "Budget": (BudgetData, True),
        "NotificationsWithSubscribers": ([NotificationWithSubscribers], False),
    }


class ActionSubscriber(AWSProperty):
    """
    `ActionSubscriber <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budgetsaction-subscriber.html>`__
    """

    props: PropsDictType = {
        "Address": (str, True),
        "Type": (str, True),
    }


class ActionThreshold(AWSProperty):
    """
    `ActionThreshold <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budgetsaction-actionthreshold.html>`__
    """

    props: PropsDictType = {
        "Type": (str, True),
        "Value": (double, True),
    }


class IamActionDefinition(AWSProperty):
    """
    `IamActionDefinition <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budgetsaction-iamactiondefinition.html>`__
    """

    props: PropsDictType = {
        "Groups": ([str], False),
        "PolicyArn": (str, True),
        "Roles": ([str], False),
        "Users": ([str], False),
    }


class ScpActionDefinition(AWSProperty):
    """
    `ScpActionDefinition <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budgetsaction-scpactiondefinition.html>`__
    """

    props: PropsDictType = {
        "PolicyId": (str, True),
        "TargetIds": ([str], True),
    }


class SsmActionDefinition(AWSProperty):
    """
    `SsmActionDefinition <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budgetsaction-ssmactiondefinition.html>`__
    """

    props: PropsDictType = {
        "InstanceIds": ([str], True),
        "Region": (str, True),
        "Subtype": (str, True),
    }


class Definition(AWSProperty):
    """
    `Definition <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budgetsaction-definition.html>`__
    """

    props: PropsDictType = {
        "IamActionDefinition": (IamActionDefinition, False),
        "ScpActionDefinition": (ScpActionDefinition, False),
        "SsmActionDefinition": (SsmActionDefinition, False),
    }


class BudgetsAction(AWSObject):
    """
    `BudgetsAction <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-budgets-budgetsaction.html>`__
    """

    resource_type = "AWS::Budgets::BudgetsAction"

    props: PropsDictType = {
        "ActionThreshold": (ActionThreshold, True),
        "ActionType": (str, True),
        "ApprovalModel": (str, False),
        "BudgetName": (str, True),
        "Definition": (Definition, True),
        "ExecutionRoleArn": (str, True),
        "NotificationType": (str, True),
        "Subscribers": ([ActionSubscriber], True),
    }
