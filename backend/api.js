const statusCodes = require('http').STATUS_CODES;
const httpConstants = require('http2').constants;
const AWS = require('aws-sdk');

AWS.config.update({ region: 'us-east-1' });

let dynamodb = new AWS.DynamoDB.DocumentClient({ apiVersion: '2012-08-10' });
