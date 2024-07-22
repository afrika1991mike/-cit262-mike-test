const AWS = require('aws-sdk');
const api = require('./api');

jest.mock('aws-sdk', () => {
  const mDocumentClient = {
    put: jest.fn().mockReturnThis(),
    promise: jest.fn()
  };
  return { DynamoDB: { DocumentClient: jest.fn(() => mDocumentClient) } };
});

describe('API tests', () => {
  let documentClient;
  
  beforeAll(() => {
    documentClient = new AWS.DynamoDB.DocumentClient();
  });

  test('should put item to DynamoDB', async () => {
    documentClient.promise.mockResolvedValue({});
    const req = { body: { event: { id: 1, name: 'test event' } } };
    const res = { writeHead: jest.fn(), end: jest.fn() };
    
    await api.events(req, res);

    expect(documentClient.put).toHaveBeenCalledWith({
      TableName: 'Events',
      Item: { id: 1, name: 'test event' }
    });
    expect(res.writeHead).toHaveBeenCalledWith(201, 'Created');
    expect(res.end).toHaveBeenCalledWith(JSON.stringify({ id: 1, name: 'test event' }));
  });
});
