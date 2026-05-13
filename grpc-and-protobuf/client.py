import grpc
import service_pb2
import service_pb2_grpc

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = service_pb2_grpc.UserServiceStub(channel)
        
        # Request data for User ID 1
        target_id = 1
        print(f"Requesting profile details for ID: {target_id}...")
        
        response = stub.GetUser(service_pb2.UserRequest(user_id=target_id))
        
        # Read the fields from the structured binary response
        print("\n--- User Profile Received ---")
        print(f"ID:      {response.id}")
        print(f"Name:    {response.name}")
        print(f"Email:   {response.email}")
        print(f"Active?: {response.is_active}")

if __name__ == '__main__':
    run()


