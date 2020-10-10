
num_test_cases = int(input())
final_output_list = []
for _ in range (num_test_cases):
    string_array = list(input().strip())
    even_array = [string_array[i] for i in range(len(string_array)) if i%2==0]
    odd_array = [string_array[i] for i in range(len(string_array)) if i%2!=0]
  
    final_output_list.append(f"{''.join(even_array)} {''.join(odd_array)}")

[print (even_odd) for even_odd in final_output_list]