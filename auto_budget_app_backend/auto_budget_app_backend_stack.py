from aws_cdk import (
    Stack,
   aws_lambda,
   aws_apigateway,
   aws_apigatewayv2
)
from constructs import Construct

class AutoBudgetAppBackendStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        create_link_token_lambda = aws_lambda.Function(
            self,
            id="CreateLinkTokenCDK",
            code=aws_lambda.Code.from_asset("./compute"),
            handler="plaid_api.create_link_token",
            runtime=aws_lambda.Runtime.PYTHON_3_10
        )

        create_link_token_integration = aws_apigateway.LambdaIntegration(
            handler=create_link_token_lambda
        )

        http_api = aws_apigatewayv2.HttpApi(self, "CreateLinkTokenApi")
        http_api.add_routes(
            path="/create_link_token",
            methods=[aws_apigatewayv2.HttpMethod.POST],
            integration=create_link_token_integration
        )
