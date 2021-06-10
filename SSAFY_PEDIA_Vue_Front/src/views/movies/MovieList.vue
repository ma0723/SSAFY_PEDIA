<template>
  <div class="container px-0">
    <div class="col">
      <div class="card" @click="movieDetail" style="height:390px; width:200px;" :class="{ dark: isDark, light: isLight }" >
        <img :src="'https://image.tmdb.org/t/p/w500/' + movie.poster_path" alt="" style="height:300px;" >
        <div class="card-body" style="overflow:hidden;">
          <p class="card-title fw-bold text-start text-nowrap overflow-hidden">{{ movie.title }} </p>
          <p class="card-title text-start">
            <i style="color:yellow;" class="fas fa-star"></i> {{ movie.vote_average }}  
          </p> 
        </div>
      </div>
      <!-- 카드 사이 간격과 이미지 사이즈 조절 필요 -->
    </div>
  </div>
</template>

<script>

export default {
  name: "MovieList",
  props: {
    movie: {
      type: Object,
      required: true
    },
  },
  methods: {
    movieDetail: function () {
      if (localStorage.getItem('jwt')) {
        this.$router.push({ name: 'MovieDetail', query: { movie: this.movie } })
      } else {
        this.$router.push({name: 'Login'})
      }
    },
  },
  computed: {
    isDark: function () {
      return this.$store.getters.isDark
    },
    isLight: function () {
      return this.$store.getters.isLight
    },
  },

}
</script>

<style>

</style>