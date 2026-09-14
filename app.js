require('dotenv').config();
const connectDB = require("./config/db"); 
const morgan = require("morgan");

const port = process.env.PORT || 4000;
connectDB();

const express = require("express");
const app = express();
const tourRouter = require("./routes/tourRouter");
const userRouter = require("./routes/userRouter");
const { unknownEndpoint } = require("./middleware/customMiddleware");




// Middleware to parse JSON
app.use(express.json());
app.use(morgan("dev"));
app.get('/', (req, res) => {
  res.send('API is running');
});


// Use the tourRouter for all "/tours" routes
app.use("/api/tours", tourRouter);

// Use the userRouter for all /users routes
app.use("/api/users", userRouter);

app.use(unknownEndpoint);
// app.use(errorHandler);

// Start the server
app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});
 
