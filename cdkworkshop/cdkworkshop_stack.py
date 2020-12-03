from hitcounter import HitCounter
from cdk_dynamo_table_viewer import TableViewer
from aws_cdk import (
    core,
    aws_lambda as _lambda,
    aws_apigateway as apigw,
)

# for testing: curl -i <url>
class CdkworkshopStack(core.Stack):

    def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # define lambda reosurces
        my_lambda = _lambda.Function(
                self, "HelloHandler",
                runtime=_lambda.Runtime.PYTHON_3_7, 
                code=_lambda.Code.asset('lambda'),
                handler='hello.handler'
         )

        # hitcounter lamnda function
        hello_with_counter = HitCounter(
            self,
            'HelloHitCounter',
            downstream=my_lambda,
        )
        
        # whenever our endpoint is hit, API Gateway will route the request to our hit counter handler,
        # which will log the hit and relay it over to the my_lambda function.
        apigw.LambdaRestApi(
             self, 
             'Endpoint',
             handler=hello_with_counter.handler,
         )

        # to view the dynamodb table         
        TableViewer(
            self,
            'Hello Hits',
            table=hello_with_counter._table
        )

        # demostrating Token
        print(my_lambda.function_name)
