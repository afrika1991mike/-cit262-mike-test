
const { greeting } = require('./helloworld');

test('should print "Hello Michael"', () => {
  expect(greeting).toBe('Hello Michael');
});