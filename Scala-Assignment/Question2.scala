package com.de.practice

import java.time.{LocalDate, Year}
import java.text.SimpleDateFormat
import java.time.format.DateTimeFormatter
import java.util.Date
import scala.collection.mutable.ListBuffer
import scala.io.Source

trait Player {
  val Year: Int
  val Name: String
  val Country: String
  val Matches: Int
  val Runs: Int
  val Wickets: Int
}
  case class Players(Year: Int, Name: String, Country: String, Matches: Int, Runs: Int, Wickets: Int) extends Player

  case class Players_with_ranks(Year: Int, Name: String, Country: String, Matches: Int, Runs: Int, Wickets: Int, Rank: Double) extends Player

  object Question2{

    private def print_player_info(playerobjects: List[Player]): Unit = {
      for (playerobject <- playerobjects) {
        println("Name : " + playerobject.Name + "\nCounty : " + playerobject.Country + "\nYear : " + playerobject.Year + "\nRuns : " + playerobject.Runs + "\nMatches : " + playerobject.Matches + "\nWickets : " + playerobject.Wickets)
        println()
      }
    }

    private def print_player_with_rank_info(playerobjects: ListBuffer[Players_with_ranks]): Unit = {
      for (playerobject <- playerobjects) {
        println("Name : " + playerobject.Name + "\nCounty : " + playerobject.Country + "\nYear : " + playerobject.Year + "\nRuns : " + playerobject.Runs + "\nMatches : " + playerobject.Matches + "\nWickets : " + playerobject.Wickets+ "\nRank : " + playerobject.Rank)
        println()
      }
    }

    def main(args:Array[String])={
      val formatter = DateTimeFormatter.ofPattern("yyyy")
      val players = Source.fromFile("src/main/scala/com/de/practice/records.txt").getLines()
        .map(line => {
          val Array(year,name,country,matches,runs,wickets) = line.split(", ")
          Players(year.toInt,name,country,matches.toInt,runs.toInt,wickets.toInt)
        })
        .toList

      println("Question - 1")
      print_player_info(players.sortBy(_.Runs)(Ordering[Int].reverse).take(1))
      println("Question - 2")
      print_player_info(players.sortBy(_.Runs)(Ordering[Int].reverse).take(5))
      println("Question - 3")
      print_player_info(players.sortBy(_.Wickets)(Ordering[Int].reverse).take(5))
      println("Question - 4")
      var list = ListBuffer[Players_with_ranks]()
      for (player_1 <- players) {
        list+=Players_with_ranks(player_1.Year,player_1.Name,player_1.Country,player_1.Matches,player_1.Runs,player_1.Wickets,5*player_1.Wickets+0.05*player_1.Runs)
      }
      print_player_with_rank_info(list.sortBy(_.Rank)(Ordering[Double].reverse).take(5))
    }
  }