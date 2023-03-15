package com.de.practice


object Question1 {
  private def get_bucket_range(n: Double): Unit = {
    var num = ((n*1000)%100).toString.format(".2f").toDouble
    println("Value : " + n)
    if (num >= 50) {
      val left = n - (num / 1000) + 0.050
      val right = n + (99 - num) / 1000
      println(f" Bucket : $left%,.3f" + " - " + f"$right%,.3f\n")
    }
    else {
      val left = n - (num / 1000)
      val right = n + (49 - num) / 1000
      println(f" Bucket : $left%,.3f" + " - " + f"$right%,.3f\n")
    }
  }
  def main(args:Array[String]): Unit = {
    val values:Array[Double]=Array(12.05, 12.03, 10.33, 11.45, 13.50)
    for (i<-values){
      get_bucket_range(i)
    }
  }
}