This file demonstrates the concept of a semaphore using a .lock mechanism. It is designed to provide an intuitive understanding of how semaphore works.

The semaphore is implemented via a .lock file to prevent concurrent access when multiple users attempt to write data at the same time. However, to fully understand and implement a more intelligent and robust solution, further study is recommended.

This file alone is not sufficient to test the behavior. A proper folder structure with appropriate user entries must be created, and multiple users must attempt to access the same task or data simultaneously.

When a .lock file is present, the server will continue attempting access. Only when the .lock file is removed (e.g., using rm -rf .lock) will the loop stop.

This logic is implemented using a while loop, as if statements are not suitable in this context. Since if statements are evaluated only once and return a true or false value, they cannot support the continuous checking behavior needed for this feature.

