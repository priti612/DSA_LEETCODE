public class Solution {
    public bool IsAnagram(string s, string t) {
        if(s.Length!=t.Length) return false;
        Char[] a=s.ToCharArray();
        Char[] b= t.ToCharArray();
        Array.Sort(a);
        Array.Sort(b);
        return new string(a)==new string(b);

    }
}