from pprint import pprint

from connect import session_hw, sample_con


def find_tag(*args):
    return session_hw.sample_airbnb.listingsAndReviews.find().limit(2)

def find_tags(*args):
    pass

def find_autor(*args):
    pass

def main():
    while True:
        user_input = input()
        action = user_input.split(':')
        match action[0]:
            case 'tag':
                result = find_tag()
                [pprint(r) for r in result]
            case 'tags':
                result = find_tags()
                # print(result)
                [pprint(r) for r in result]
            case 'autor':
                result = find_autor()
                [pprint(r) for r in result]
            case 'exit':
                break
            case _:
                print("Unknown command")

if __name__ == "__main__":
    main()