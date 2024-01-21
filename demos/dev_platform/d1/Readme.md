
# Getting started with Cloudflare D1

D1 is Cloudflare’s native serverless SQL database. D1 allows you to build applications that handle large amounts of users at no extra cost

## Prerequisites

 *  Sign up for a Cloudflare Account : `https://dash.cloudflare.com/sign-up`
 *  Install npm: `https://docs.npmjs.com/getting-started`
 *  Install Node.js: `https://nodejs.org/en/`
 *  Install Wrangler within your project using npm and Node.js: `npm install wrangler --save-dev` 

### 1. Login to your account
```
$ make login
```

### 2. Create a Worker project
```
$ make create_worker d1-demo
```
When setting up your `d1-demo` Worker, answer the questions as below:
*  Your directory has been titled kv-tutorial.
*  Choose `"Hello World" Worker` for the type of application.
*  Select `yes` to using TypeScript.
*  Select `yes` to using Git.
*  Select `no` to deploying.


### 3. Create a database
```
make create_database <DATABASE_NAME>
```

#### Bind your namespace to your worker
In your `wrangler.toml` file, add the following with the values generated in your terminal:
```wrangler.toml
[[d1_databases]]
binding = "DB" # available in your Worker on env.DB
database_name = "prod-d1-tutorial"
database_id = "<unique-ID-for-your-database>"
```

### 4. Run a query against your D1 database
Create a `schema.sql` file
```
$ cd d1-demo
$ touch schema.sql
```
Append the following code
```
DROP TABLE IF EXISTS Customers;
CREATE TABLE IF NOT EXISTS Customers (CustomerId INTEGER PRIMARY KEY, CompanyName TEXT, ContactName TEXT);
INSERT INTO Customers (CustomerID, CompanyName, ContactName) VALUES (1, 'Alfreds Futterkiste', 'Maria Anders'), (4, 'Around the Horn', 'Thomas Hardy'), (11, 'Bs Beverages', 'Victoria Ashworth'), (13, 'Bs Beverages', 'Random Name');
```
Interact with D1
```
$ make list_databases
$ make delete_database <DATABASE_NAME>
$ make exucute_query <DATABASE_NAME> <PATH_TO_SQL_COMMANDS_FILE>
```

### 5. Interact with your D1 (with workers)
Replace the `src/index.ts` file with the following code.
```
export interface Env {
  // If you set another name in wrangler.toml as the value for 'binding',
  // replace "DB" with the variable name you defined.
  DB: D1Database;
}

export default {
  async fetch(request: Request, env: Env) {
    const { pathname } = new URL(request.url);

    if (pathname === "/api/beverages") {
      // If you did not use `DB` as your binding name, change it here
      const { results } = await env.DB.prepare(
        "SELECT * FROM Customers WHERE CompanyName = ?"
      )
        .bind("Bs Beverages")
        .all();
      return Response.json(results);
    }

    return new Response(
      "Call /api/beverages to see everyone who works at Bs Beverages"
    );
  },
};
```

### 6. Deploy your worker to Cloudflare's global network
```
$ make deploy
```


Enjoy!
