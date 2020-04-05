"""
Helper functions for python-layer
"""
import boto3


def read_layer(path, loader=None, binary_file=False):
    open_mode = "rb" if binary_file else "r"
    with open(path, mode=open_mode) as fh:
        if not loader:
            return fh.read()
        return loader(fh.read())


def get_client(
    client=None,
    profile_name=None,
    aws_access_key_id=None,
    aws_secret_access_key=None,
    region=None,
):
    """Shortcut for getting an initialized instance of the boto3 client."""
    #
    # boto3.setup_default_session(
    #     profile_name=profile_name,
    #     aws_access_key_id=aws_access_key_id,
    #     aws_secret_access_key=aws_secret_access_key,
    #     region_name=region,
    # )
    # # return boto3.client(client)
    return boto3.client("lambda")


def get_layer_arn(layer: dict) -> str:
    """

    :param layer:
    :return:
    """
    return layer["Layer_arn"] + ":" + str(layer["Layer_version"])
