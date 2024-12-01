from collections import Counter

def main():
    text = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt
    ut labore et dolore magna aliqua. Dolor sed viverra ipsum nunc aliquet bibendum enim. In
    massa tempor nec feugiat. Nunc aliquet bibendum enim facilisis gravida. Nisl nunc mi ipsum
    faucibus vitae aliquet nec ullamcorper. Amet luctus venenatis lectus magna fringilla. Volutpat maecenas volutpat blandit aliquam etiam erat velit scelerisque in. Egestas egestas fringilla
    phasellus faucibus scelerisque eleifend. Sagittis orci a scelerisque purus semper eget duis. Nulla
    pharetra diam sit amet nisl suscipit. Sed adipiscing diam donec adipiscing tristique risus nec
    feugiat in. Fusce ut placerat orci nulla. Pharetra vel turpis nunc eget lorem dolor. Tristique
    senectus et netus et malesuada."""
    
    text = text.replace(',', '').replace('.', '').lower()
    textList = text.split()
    
    count = Counter(textList); print(count)
    unique = set(textList); print(unique)
    print(unique)
main()
