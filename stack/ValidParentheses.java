public class Solution {
public boolean isValid(String s) {
Stack<Character> stack = new Stack<Character>();
for (char c: s.toCharArray()) {
if (c=='(')
stack.push(')');
else if (c == '{')
stack.push('}');
else if (c == '[')
stack.push(']');
else if (stack.isEmpty() || stack.pop() != c)
return false;
} return stack.isEmpty();
}
}

#这题记得push反括号，然后pop出来的比较