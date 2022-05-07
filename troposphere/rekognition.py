# Copyright (c) 2012-2022, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***


from . import AWSObject, AWSProperty, PropsDictType, Tags
from .validators import boolean, double
from .validators.rekognition import validate_PolygonRegionsOfInterest


class Collection(AWSObject):
    """
    `Collection <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rekognition-collection.html>`__
    """

    resource_type = "AWS::Rekognition::Collection"

    props: PropsDictType = {
        "CollectionId": (str, True),
        "Tags": (Tags, False),
    }


class Project(AWSObject):
    """
    `Project <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rekognition-project.html>`__
    """

    resource_type = "AWS::Rekognition::Project"

    props: PropsDictType = {
        "ProjectName": (str, True),
    }


class BoundingBox(AWSProperty):
    """
    `BoundingBox <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rekognition-streamprocessor-boundingbox.html>`__
    """

    props: PropsDictType = {
        "Height": (double, True),
        "Left": (double, True),
        "Top": (double, True),
        "Width": (double, True),
    }


class ConnectedHomeSettings(AWSProperty):
    """
    `ConnectedHomeSettings <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rekognition-streamprocessor-connectedhomesettings.html>`__
    """

    props: PropsDictType = {
        "Labels": ([str], True),
        "MinConfidence": (double, False),
    }


class DataSharingPreference(AWSProperty):
    """
    `DataSharingPreference <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rekognition-streamprocessor-datasharingpreference.html>`__
    """

    props: PropsDictType = {
        "OptIn": (boolean, True),
    }


class FaceSearchSettings(AWSProperty):
    """
    `FaceSearchSettings <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rekognition-streamprocessor-facesearchsettings.html>`__
    """

    props: PropsDictType = {
        "CollectionId": (str, True),
        "FaceMatchThreshold": (double, False),
    }


class KinesisDataStream(AWSProperty):
    """
    `KinesisDataStream <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rekognition-streamprocessor-kinesisdatastream.html>`__
    """

    props: PropsDictType = {
        "Arn": (str, True),
    }


class KinesisVideoStream(AWSProperty):
    """
    `KinesisVideoStream <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rekognition-streamprocessor-kinesisvideostream.html>`__
    """

    props: PropsDictType = {
        "Arn": (str, True),
    }


class NotificationChannel(AWSProperty):
    """
    `NotificationChannel <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rekognition-streamprocessor-notificationchannel.html>`__
    """

    props: PropsDictType = {
        "Arn": (str, True),
    }


class S3Destination(AWSProperty):
    """
    `S3Destination <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rekognition-streamprocessor-s3destination.html>`__
    """

    props: PropsDictType = {
        "BucketName": (str, True),
        "ObjectKeyPrefix": (str, False),
    }


class StreamProcessor(AWSObject):
    """
    `StreamProcessor <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rekognition-streamprocessor.html>`__
    """

    resource_type = "AWS::Rekognition::StreamProcessor"

    props: PropsDictType = {
        "BoundingBoxRegionsOfInterest": ([BoundingBox], False),
        "ConnectedHomeSettings": (ConnectedHomeSettings, False),
        "DataSharingPreference": (DataSharingPreference, False),
        "FaceSearchSettings": (FaceSearchSettings, False),
        "KinesisDataStream": (KinesisDataStream, False),
        "KinesisVideoStream": (KinesisVideoStream, True),
        "KmsKeyId": (str, False),
        "Name": (str, False),
        "NotificationChannel": (NotificationChannel, False),
        "PolygonRegionsOfInterest": (validate_PolygonRegionsOfInterest, False),
        "RoleArn": (str, True),
        "S3Destination": (S3Destination, False),
        "Tags": (Tags, False),
    }


class Point(AWSProperty):
    """
    `Point <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rekognition-streamprocessor-point.html>`__
    """

    props: PropsDictType = {
        "X": (double, True),
        "Y": (double, True),
    }
