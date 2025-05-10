"""Configuration as per env - dev, staging and prod"""
import os
import json


class Config:
    """Configurations"""
    def deploy_environment():
        """Deployment as per environment"""

        dirname = os.path.dirname(__file__)
        # Load variables common to all environment
        props = open(os.path.join(dirname, "props.json"))
        print(type(props))
        print(props)

        prop_dict = json.load(props)
        # prop_dict['environment'] = os.environ['ENVIRONMENT']
        prop_dict['aws_account'] = os.environ['AWS_ACCOUNT']
        prop_dict['aws_region'] = os.environ['AWS_REGION']
        return prop_dict
