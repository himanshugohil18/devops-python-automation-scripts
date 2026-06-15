import os

print("===== Docker Cleanup Started =====")

print("\nRemoving stopped containers...")
os.system(
    "docker container prune -f"
)

print("\nRemoving unused images...")
os.system(
    "docker image prune -a -f"
)

print("\nRemoving unused volumes...")
os.system(
    "docker volume prune -f"
)

print("\nRemoving unused networks...")
os.system(
    "docker network prune -f"
)

print(
    "\nDocker cleanup completed!"
)