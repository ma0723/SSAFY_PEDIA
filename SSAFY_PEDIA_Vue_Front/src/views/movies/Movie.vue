<template>
  <div>
    <p class="title-font"> Top Rating Movies </p>
    <Movies :movies="high_movies" />
    <p class="title-font"> Bottom Rating Movies </p>
    <Movies :movies="low_movies" />
    <p class="title-font"> New Movies </p>
    <Movies :movies="recent_movies" />
    <p class="title-font"> Old Movies </p>
    <Movies :movies="old_movies" />
  </div>
</template>

<script>
import Movies from '@/views/movies/Movies.vue'

import axios from 'axios'

export default {
  name: "Movie",
  components: {
    Movies,
  },
  data: function () {
    return {
      high_movies: [],
      low_movies: [],
      recent_movies: [],
      old_movies: [],
      // 개봉일순, 평점순
      random_movies: [],
      // 전체 영화 데이터 받아서 무작위 랜덤
      // movies/views.py의 recommend 함수에는 serializer을 5개로 리스트에 담아 보내고 있어서
      // 5개의 데이터 초기값이 반드시 필요해요!
    }
  },
  methods: {
    getRecommend: function () {
      // 개봉일순, 평점순 추천
      axios({
        method: 'get',
        url: `https://ssafypedia.link/movies/recommend/`,
      })
      .then((res) => {
        this.high_movies = res.data[0]
        this.low_movies = res.data[1]
        this.recent_movies = res.data[2]
        this.old_movies = res.data[3]
      })
      .catch( (err) => {
        console.log(err)
      })
    },
  },
  created: function () {
    this.getRecommend()
  },
}
</script>

<style>
.light {
  color: #2c3e50;
}
.dark {
  background-color: rgba(0, 0, 0, 0.911);
  color: white
}
</style>