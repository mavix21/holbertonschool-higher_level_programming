#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

if (!url) {
  console.error('Please, provide an url');
  process.exit(1);
}

request.get(url, (error, response, body) => {
  if (error) {
    console.error(`Error: ${error.message}`);
    return;
  }

  const completedTasksByUser = {};
  const allTasks = JSON.parse(body); // array of task objects
  for (const task of allTasks) {
    if (task.completed) {
      if (task.userId in completedTasksByUser) {
        completedTasksByUser[task.userId] += 1;
      } else {
        completedTasksByUser[task.userId] = 1;
      }
    }
  }

  console.log(completedTasksByUser);
});
