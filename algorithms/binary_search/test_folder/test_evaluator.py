import time


def evaluate_test_cases(func, tests):

    results = []
    total_tests = len(tests)

    passed_count = 0
    failed_count = 0

    for idx, test_case in enumerate(tests):
        try:
            input_data = test_case['input'] 
            expected_output = test_case['output']

            start_time = time.time()
            result = func(**input_data)
            execution_time = round((time.time() - start_time) * 1000, 3)

            if result == expected_output:
                print(f"---> TEST CASE #{idx + 1}\n")
                print("Input:", input_data)
                print("\nExpected Output:", expected_output)
                print("\nActual Output:", result)
                print(f"\nExecution Time: {execution_time} ms")
                print("\nTest Result: PASSED\n")
                passed_count += 1
            else:
                print(f"---> TEST CASE #{idx + 1}\n")
                print("Input:", input_data)
                print("\nExpected Output:", expected_output)
                print("\nActual Output:", result)
                print(f"\nExecution Time: {execution_time} ms")
                print("\nTest Result: FAILED\n")
                failed_count += 1

            results.append((result, result == expected_output, execution_time))

        except Exception as e:
            print(f"Error occurred while processing test case #{idx + 1}: {e}")
            print("Test case data:", test_case)
            print("Skipping this test case.")
            print()

            failed_count += 1

    print("### SUMMARY ###\n")
    print(f"TOTAL: {total_tests}, PASSED: {passed_count}, FAILED: {failed_count}\n")
    print(results, "\n")
