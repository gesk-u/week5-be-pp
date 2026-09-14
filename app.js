require('dotenv').config();
const connectDB = require("./config/db"); 
const morgan = require("morgan");

const port = process.env.PORT || 4000;
connectDB();

const express = require("express");
const app = express();
const tourRouter = require("./routes/tourRouter");
const userRouter = require("./routes/userRouter");
const { unknownEndpoint, errorHandler } = require("./middleware/customMiddleware");

// Middleware to parse JSON
app.use(express.json());
app.use(morgan("dev"));
app.get('/', (req, res) => {
  res.send('API is running');
});

app.get('/error', (req, res, next) => {
  const error = new Error("Network problem");
  next(error);
});

// Use the tourRouter for all "/tours" routes
app.use("/api/tours", tourRouter);

// Use the userRouter for all /users routes
app.use("/api/users", userRouter);

// Use the unknownEndpoint middleware for handling undefined routes
app.use(unknownEndpoint);

// Use the errorHandler middleware for handling errors
app.use(errorHandler);

// Start the server
app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});
 
