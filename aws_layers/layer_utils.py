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
    profile_name=None, region=None,
):
    """Shortcut for getting an initialized instance of the boto3 client."""
    boto3.setup_default_session(profile_name=profile_name, region_name=region)
    return boto3.client("lambda")


def get_layer_arn(layer: dict) -> str:
    """

    :param layer:
    :return:
    """
    return layer["Layer_arn"] + ":" + str(layer["Layer_version"])


def get_current_lambda_layers(boto3_client: object, function_name: str) -> list:
    """
    Return the current layers of the lambda function
    """
    lambda_config = boto3_client.get_function_configuration(FunctionName=function_name)
    current_layers = lambda_config.get("Layers", [])
    return [] if not current_layers else [obj["Arn"] for obj in lambda_config["Layers"]]
