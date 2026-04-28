import algorithm.binary_search.binary_search as binary_search
import algorithm.exponential_search.exponential_search as exponential_search
import algorithm.interpolation_search.interpolation_search as interpolation_search
import algorithm.linear_search.linear_search as linear_search
import algorithm.jump_search.jump_search as jump_search


def main():
    arr = [18, 22, 83, 154, 165, 176, 237, 248, 289, 300]
    target = 165

    
    print("Binary Search Result:", binary_search.binary_search(arr, target))
    print("Exponential Search Result:", exponential_search.exponential_search(arr, target))
    print("Interpolation Search Result:", interpolation_search.interpolation_search(arr, target))
    print("Linear Search Result:", linear_search.linear_search(arr, target))
    print("Jump Search Result:", jump_search.jump_search(arr, target))
    
    
if __name__ == "__main__":
    main()