# WebSockets and Real-Time Systems

WebSockets are protocols providing full-duplex (two-way) communication over a single, long-lived TCP connection, allowing servers to send data to clients instantly without requests. Real-time systems leverage this to deliver data instantly (like chat, stock updates, or gaming), crucial for apps requiring low-latency interaction.


## WebSockets Explained

Unlike HTTP, which opens and closes connections for every request (unidirectional), WebSockets stay open, reducing overhead.

- Handshake: It starts as an HTTP request, then upgrades to a ws: or wss: (secure) connection.

- Bidirectional: Both client and server can send messages at any time, allowing for rapid, back-and-forth communication.

- Persistent: The connection remains open until closed by either party, making it ideal for continuous, live data streaming.



## Real-time Systems

Real-time systems process input data immediately, usually within milliseconds.

- Key Use Cases: Live chat apps, collaborative editing (e.g., Google Docs), multiplayer games, live dashboard analytics, and stock/crypto ticker updates.

- Data Delivery: Unlike traditional polling (where the client asks for new data every few seconds), WebSocket servers push data directly to the client as soon as it's available.



## Advantages and Considerations

- Lower Latency: No need to re-establish connections, ensuring near-instantaneous messaging.

- Efficiency: Header data is smaller than HTTP requests, reducing network load.

- Complexity: Requires careful handling of connection drops, reconnections, and server-side state management (e.g., using heartbeat mechanisms).



## Running Demo Code

```bash
pip install websockets
```

```bash
python server.py
```

```bash
python client.py
```

