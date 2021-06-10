<template>
  <div class="col">
    <input type="text" v-model.trim="content" @keyup.enter="createComment" class="mx-2">
    <button type="button" class="btn btn-sm" @click="createComment" :class="{ 'btn-outline-dark': isLight, 'btn-outline-light': isDark }">Comment Create</button>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: "CreateComment",
  data: function () {
    return {
      content: null,
    }
  },
  props: {
    review: {
      type: Object,
      required: true
    }
  },
  methods: {
    setToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },
    createComment: function () {
      const comment = {
        content: this.content,
      }
      
      if (comment.content) {
        axios({
          method: 'post',
          url: `https://ssafypedia.link/movies/review/${this.review.id}/comment/`,
          data: comment,
          headers: this.setToken()
        })
        .then((res) => {
          console.log(res)
          this.content = null
          this.$emit('create-comment')
        })
        .catch((err) => {
          console.log(err)
        })
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