
# Getting started with Cloudflare Hyperdrive

Turn your existing regional database into a globally distributed database.

## Prerequisites

 *  Sign up for a Cloudflare Account : `https://dash.cloudflare.com/sign-up`
 *  Install npm: `https://docs.npmjs.com/getting-started`
 *  Install Node.js: `https://nodejs.org/en/`
 *  Install Wrangler within your project using npm and Node.js: `npm install wrangler --save-dev` 
 *  A publicly accessible PostgreSQL (or PostgreSQL compatible) database (we recommend Neon `https://neon.tech/` for this demo)

### 1. Login to your account
```
$ make login
```

### 2. Create a Worker project
```
$ make create_worker hd-demo
```
When setting up your `hd-demo` Worker, answer the questions as below:
*  Your directory has been titled kv-tutorial.
*  Choose `"Hello World" Worker` for the type of application.
*  Select `yes` to using TypeScript.
*  Select `yes` to using Git.
*  Select `no` to deploying.


### 3. Connect Hyperdrive to a database
```
make create_hyperdrive_conn <NAME> <CONNECTION_STRING>

# Example of <CONNECTION_STRING>:  postgres://USERNAME:PASSWORD@HOSTNAME_OR_IP_ADDRESS:PORT/database_name
```

#### Bind your namespace to your worker
In your `wrangler.toml` file, add the following with the values generated in your terminal:
```
node_compat = true # required for database drivers to function

[[hyperdrive]]
binding = "HYPERDRIVE"
id = "a76a99bc342644deb02c38d66082262a" # the ID associated with the Hyperdrive you just created
```

### 4. Interact with Hyperdrive
```
@echo "make create_hyperdrive_conn <NAME> <CONNECTION_STRING>"
@echo "make list_hyperdrive_conns"
@echo "make delete_hyperdrive_conn <ID>"
@echo "make get_hyperdrive_conn <ID>" 
```

### 5. Run a query against your database (with workers)
Install `node-postgres`
```
$ cd hd-demo
$ npm i pg
```
Replace the `src/index.ts` file with the following code.
```
import { Client } from 'pg';

export interface Env {
	// If you set another name in wrangler.toml as the value for 'binding',
	// replace "HYPERDRIVE" with the variable name you defined.
	HYPERDRIVE: Hyperdrive;
}

export default {
	async fetch(request: Request, env: Env, ctx: ExecutionContext) {
		console.log(JSON.stringify(env))
		// Create a database client that connects to your database via Hyperdrive
		// Hyperdrive generates a unique connection string you can pass to
		// supported drivers, including node-postgres, Postgres.js, and the many
		// ORMs and query builders that use these drivers.
		const client = new Client({ connectionString: env.HYPERDRIVE.connectionString });

		try {
			// Connect to your database
			await client.connect();

			// Test query
			const result = await client.query({ text: 'SELECT * FROM pg_tables' });

			// Return result rows as JSON
			return Response.json({ result: result });
		} catch (e) {
			console.log(e);
			return Response.json({ error: JSON.stringify(e) }, { status: 500 });
		}
	},
};
```

### 6. Deploy your worker to Cloudflare's global network
```
$ make deploy
```


Enjoy!
