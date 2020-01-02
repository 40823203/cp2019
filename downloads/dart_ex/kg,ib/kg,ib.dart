main(){  
//字串temp為[40C,80C,50F,40C,25F]
 List temp = [' 25kg', ' 30lb',' 56lb',' 14kg',' 68lb','198kg'];
  for (var i in temp) {
  var a = int.parse(i[0]+i[1]+i[2]);
  //將字串轉數字
    if (i[4] == "g") {
    double k=a*(2.2);
    print("$i=$k Ib");
}
    else{ 
    double m=a*0.45;
    print("$i=$m Kg");

}
}
}