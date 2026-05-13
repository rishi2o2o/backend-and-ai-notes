### What is Protobuf (Protocol Buffer)

Protobuf is open-source, language-neutral mechanism for serializing structured data.

* Binary Format: Unlike JSON or XML (which are text-based), Protobuf converts data into a compact binary format that is much smaller and faster to process.

* Contract-First: You define your data structures in a .proto file. This acts as a single source of truth (a contract) between the client and server.

* Code Generation: Using the Protobuf compiler (protoc), you can automatically generate native code for C++, Java, Python, Go, and more.

* Strongly Typed: It ensures that both sides agree on exactly what data is being sent, preventing errors common in loosely-typed JSON APIs.



### What is gRPC (Remote Procedure Call)

gRPC is a modern, open-source framework developed by Google that enables an application to call a function on a different machine as if it were a local function call.

* Built on HTTP/2: It leverages HTTP/2 features like multiplexing (sending many requests over one connection) and header compression to reduce latency.

* Four Streaming Modes:
  - Unary: Simple request/response.
  - Server Streaming: One request, multiple responses.
  - Client Streaming: Multiple requests, one response.
  - Bidirectional: Real-time, two-way communication.

* Language Agnostic: A Java server can communicate seamlessly with a Python client because they both use the same Protobuf contract.



### Example workflow

1. You write a .proto file defining a User message and a GetUser service.

2. Use protoc to generate a User class and a UserClient stub in your preferred languages.

3. The server implements the logic; the client calls the GetUser() function.

4. Data is packed into binary via Protobuf and sent over HTTP/2 via gRPC.



### How to run example code

1. Install gRPC tools for Python

    ```bash
    pip install grpcio grpcio-tools
    ```

2. Run protobuf compiler (protoc) to generate network communication code

    ```bash
    python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. service.proto
    ```

3. Start the server

    ```bash
    python server.py
    ```

4. Send request from client

    ```bash
    python client.py
    ```



