package com.de.practice

import java.time.{LocalDate, Year}
import java.text.SimpleDateFormat
import java.time.format.DateTimeFormatter
import java.util.Date
import scala.collection.mutable.ListBuffer
import scala.io.Source

trait Player{
  val year: Int
  val player_name: String
  val country: String
  val matches: Int
  val runs: Int
  val wickets: Int
}

case class Players(year: Int, player_name: String, country: String, matches: Int, runs: Int, wickets: Int) extends Player

case class Player_Ranks(year: Int, player_name: String, country: String, matches: Int, runs: Int, wickets: Int, Rank: Double) extends Player

object Question2{
    private def get_player_info(player: List[Player]): Unit = {
      for (playerobject <- player) {
        println("Name : " + playerobject.player_name + "\nCountry : " + playerobject.country + "\nYear : " + playerobject.year + "\nRuns : " + playerobject.runs + "\nMatches : " + playerobject.matches + "\nWickets : " + playerobject.wickets)
        println()
      }
    }

    private def get_player_ranks_info(playerobjects: ListBuffer[Player_Ranks]): Unit = {
      for (playerobject <- playerobjects) {
        println("Player Name : " + playerobject.player_name + "\nCountry : " + playerobject.country + "\nYear : " + playerobject.year + "\nRuns : " + playerobject.runs + "\nMatches : " + playerobject.matches + "\nWickets : " + playerobject.wickets+ "\nRank : " + playerobject.Rank)
        println()
      }
    }

    def main(args:Array[String])={
      val players = Source.fromFile("src/main/scala/com/de/practice/records.txt").getLines()
        .map(line => {
          val Array(year,name,country,matches,runs,wickets) = line.split(", ")
          Players(year.toInt,name,country,matches.toInt,runs.toInt,wickets.toInt)
        })
        .toList

//      println(players)

      println("Query 1: Player with the best highest run scored.")
      get_player_info(players.sortBy(_.runs)(Ordering[Int].reverse).take(1))
      println("Query 2: Top 5 players by run scored")
      get_player_info(players.sortBy(_.runs)(Ordering[Int].reverse).take(5))
      println("Query 3: Top 5 players by wicket taken.")
      get_player_info(players.sortBy(_.wickets)(Ordering[Int].reverse).take(5))
      println("Query 4: Rank players with overall performance give weight 5x to wicket taken and (5/100)x to run scored.")
      var list = ListBuffer[Player_Ranks]()
      for (player_1 <- players) {
        list+=Player_Ranks(player_1.year,player_1.player_name,player_1.country,player_1.matches,player_1.runs,player_1.wickets,5*player_1.wickets+0.05*player_1.runs)
      }
      get_player_ranks_info(list.sortBy(_.Rank)(Ordering[Double].reverse).take(5))
    }
  }