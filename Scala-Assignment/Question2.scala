package com.de.practice

import java.time.{LocalDate, Year}
import java.text.SimpleDateFormat
import java.time.format.DateTimeFormatter
import java.util.Date
import scala.collection.mutable.ListBuffer
import scala.io.Source


//trait for player with all the required fields
trait Player{
  val year: Int
  val player_name: String
  val country: String
  val matches: Int
  val runs: Int
  val wickets: Int
}

case class Players(year: Int, player_name: String, country: String, matches: Int, runs: Int, wickets: Int) extends Player

object Question2{
    private def get_player_info(players: List[Player]): Unit = {
      for (player <- players) {
        println(
        s"""
          Name : ${player.player_name}
          Country : ${player.country}
          Year : ${player.year}
          Runs : ${player.runs}
          Matches : ${player.matches}
          Wickets : ${player.wickets}
            """)
      }
    }

    def main(args:Array[String])={
      val players = Source.fromFile("src/main/scala/com/de/practice/records.txt").getLines()
        .map(line => {
          val Array(year,name,country,matches,runs,wickets) = line.split(", ")
          Players(year.toInt,name,country,matches.toInt,runs.toInt,wickets.toInt)
        })
        .toList


      println("Query 1: Player with the best highest run scored.")
      get_player_info(players.sortBy(_.runs)(Ordering[Int].reverse).take(1))
      println("Query 2: Top 5 players by run scored")
      get_player_info(players.sortBy(_.runs)(Ordering[Int].reverse).take(5))
      println("Query 3: Top 5 players by wicket taken.")
      get_player_info(players.sortBy(_.wickets)(Ordering[Int].reverse).take(5))
      println("Query 4: Rank players with overall performance give weight 5x to wicket taken and (5/100)x to run scored.")
      get_player_info(players.sortBy(player => 5*player.wickets + 0.05*player.runs)(Ordering[Double].reverse).take(5))
    }
  }