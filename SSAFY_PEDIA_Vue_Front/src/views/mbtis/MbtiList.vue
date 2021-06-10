<template>
  <div class="container">
    <div class="col mx-2">
      <div class="card" @click="movieDetail" style="height:400px; width:200px;" :class="{ dark: isDark, light: isLight }" >
        <img :src="'https://image.tmdb.org/t/p/w500/' + movie.poster_path" alt="" style="height:300px;" >
        <div class="card-body mx-1" style="overflow:hidden;">
          <p class="fs-5 fw-bold text-start text-nowrap overflow-hidden">{{ movie.title }} </p>
          <p class="fs-6 text-start">
            <i style="color:yellow;" class="fas fa-star"></i> {{ movie.vote_average }} 
          </p> 
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "MbtiList",
  props: {
    movie: {
      type: Object,
      required: true
    },
  },
  methods: {
    movieDetail: function () {
      if (localStorage.getItem('jwt')) {
        console.log(this.movie)
        this.$router.push({ name: 'MbtiDetail', query: { movie: this.movie } })
      } else {
        this.$router.push({name: 'Login'})
      }
    }
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