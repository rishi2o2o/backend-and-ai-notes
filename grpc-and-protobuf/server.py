import grpc
from concurrent import futures
import service_pb2
import service_pb2_grpc

USER_DATABASE = {
    1: {"name": "Alice Smith", "email": "alice@example.com", "is_active": True},
    2: {"name": "Bob Jones", "email": "bob@example.com", "is_active": False}
}

class UserServicer(service_pb2_grpc.UserServiceServicer):
    def GetUser(self, request, context):
        print(f"Server looking for User ID {request.user_id}...")
        
        user_data = USER_DATABASE.get(request.user_id)
        
        if user_data:
            print(f"Sent details for User ID {request.user_id}")
            return service_pb2.UserResponse(
                id=request.user_id,
                name=user_data["name"],
                email=user_data["email"],
                is_active=user_data["is_active"]
            )
        else:
            print(f"User ID not found. Sending emtpy response.")
            return service_pb2.UserResponse(
                id=0, 
                name="Unknown", 
                email="", 
                is_active=False
            )

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    service_pb2_grpc.add_UserServiceServicer_to_server(UserServicer(), server)
    server.add_insecure_port('[::]:50051')
    print("User gRPC Server running on port 50051...")
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()


