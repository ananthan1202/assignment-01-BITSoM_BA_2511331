// OP1: insertMany() – insert all 3 documents

db.products.insertMany([
  {
    name: "iPhone 15",
    category: "Electronics",
    price: 75000,
    brand: "Apple",
    warranty_years: 1
  },
  {
    name: "Men's Denim Jacket",
    category: "Clothing",
    price: 2500,
    brand: "Levis"
  },
  {
    name: "Amul Milk",
    category: "Groceries",
    price: 60,
    expiry_date: new Date("2024-12-01")
  }
])

// OP2: find() – retrieve all Electronics products with price > 20000

db.products.find({
  category: "Electronics",
  price: { $gt: 20000 }
})

// OP3: find() – retrieve all Groceries expiring before 2025-01-01

db.products.find({
  category: "Groceries",
  expiry_date: { $lt: new Date("2025-01-01") }
})

// OP4: updateOne() – add discount_percent field

db.products.updateOne(
  { name: "iPhone 15" },
  { $set: { discount_percent: 10 } }
)

// OP5: createIndex() – index on category

db.products.createIndex({ category: 1 })
