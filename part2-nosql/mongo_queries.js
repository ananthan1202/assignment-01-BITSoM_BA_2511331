// Q1
db.customers.find()

// Q2
db.customers.find({customer_id: 1})

// Q3
db.customers.aggregate([
  {$unwind: "$orders"}
])
