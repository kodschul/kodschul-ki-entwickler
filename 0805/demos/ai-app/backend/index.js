const express = require('express');
const cors = require('cors');
const { ApolloServer } = require('@apollo/server');
const { expressMiddleware } = require('@apollo/server/express4');
const bodyParser = require('body-parser');
const { randomUUID } = require('crypto');

// In-memory data store
let todos = [
  { id: randomUUID(), title: 'Learn GraphQL', completed: false, createdAt: new Date().toISOString() },
  { id: randomUUID(), title: 'Build a fullstack app', completed: false, createdAt: new Date().toISOString() },
];

const typeDefs = `#graphql
  type Todo {
    id: ID!
    title: String!
    completed: Boolean!
    createdAt: String!
  }

  type Query {
    todos: [Todo!]!
    todo(id: ID!): Todo
  }

  type Mutation {
    createTodo(title: String!): Todo!
    toggleTodo(id: ID!): Todo
    deleteTodo(id: ID!): Boolean!
  }
`;

const resolvers = {
  Query: {
    todos: () => todos,
    todo: (_, { id }) => todos.find(t => t.id === id) || null,
  },
  Mutation: {
    createTodo: (_, { title }) => {
      const todo = {
        id: randomUUID(),
        title,
        completed: false,
        createdAt: new Date().toISOString(),
      };
      todos.push(todo);
      return todo;
    },
    toggleTodo: (_, { id }) => {
      const todo = todos.find(t => t.id === id);
      if (!todo) return null;
      todo.completed = !todo.completed;
      return todo;
    },
    deleteTodo: (_, { id }) => {
      const index = todos.findIndex(t => t.id === id);
      if (index === -1) return false;
      todos.splice(index, 1);
      return true;
    },
  },
};

async function startServer() {
  const app = express();

  app.use(cors({ origin: 'http://localhost:5173' }));
  app.use(bodyParser.json());

  const server = new ApolloServer({ typeDefs, resolvers });
  await server.start();

  app.use('/graphql', expressMiddleware(server));

  app.listen(4000, () => {
    console.log('GraphQL API running at http://localhost:4000/graphql');
  });
}

startServer();
