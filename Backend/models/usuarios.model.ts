import mongoose from "mongoose";

export interface usuarios extends mongoose.Document {
   
    name: String,
    lastname: String,
    email: String,
    password: String,
    phoneNumber: String,
    address: String,
}