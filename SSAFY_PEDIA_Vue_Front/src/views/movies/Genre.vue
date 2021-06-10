<template>
  <div>    
    <p class="title-font"> Action Movies </p>
    <Movies :movies="action_movies" />
    <p class="title-font"> Animation Movies </p>
    <Movies :movies="animation_movies" />
    <p class="title-font"> Thriller Movies </p>
    <Movies :movies="thriller_movies" />
    <p class="title-font"> Fantasy Movies </p>
    <Movies :movies="fantasy_movies" />
    <p class="title-font"> Comedy Movies </p>  
    <Movies :movies="comedy_movies" />
    <p class="title-font"> SF Movies </p>
    <Movies :movies="sf_movies" />
  </div>
</template>

<script>
import axios from 'axios'
import Movies from '@/views/movies/Movies.vue'
export default {
  name: "Genre",
  components: {
    Movies,
  },
  data: function () {
    return {
      action_movies : [],
      animation_movies : [],
      thriller_movies : [],
      fantasy_movies : [], 
      comedy_movies : [], 
      romance_movies : [], 
      sf_movies : [],       
      // 7개 장르별 영화 초기값
    }
  },
  methods: {
    getGenre: function () {
      axios({
        method: 'get',
        url: `https://ssafypedia.link/movies/genre/`,
      })
      .then((res) => {
        this.action_movies = res.data[0]
        this.animation_movies = res.data[1]
        this.thriller_movies = res.data[2]
        this.fantasy_movies = res.data[3]
        this.comedy_movies = res.data[4]
        this.romance_movies = res.data[5]
        this.sf_movies = res.data[6]
      })
      .catch( (err) => {
          console.log(err)
      })
    },
  },
  created: function () {
    this.getGenre()
    // 생성되지마자 실행되도록 created에 함수 넣기
  },
}
</script>

<style>

</style>