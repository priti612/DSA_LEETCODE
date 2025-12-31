class Solution {
    public boolean isIsomorphic(String s, String t) {
      if(s.length() !=t.length())
      return false;
      Map<Character,Character>mp=new HashMap<>();
      for(int i=0;i<s.length();i++){
        char original=s.charAt(i);
        char rep=t.charAt(i);
if(!mp.containsKey(original)){
    if(!mp.containsValue(rep))
    mp.put(original,rep);
    else
    return false;
}
else{
    char mpp=mp.get(original);
    if(mpp!=rep)
    return false;
}

      }
      return true;  

    }

}