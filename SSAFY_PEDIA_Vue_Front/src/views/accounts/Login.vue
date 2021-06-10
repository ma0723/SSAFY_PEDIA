<template>
  <div>
    <p class="title-font">Login Page</p>
    <div class="mt-2">
      <label for="username" class="title-font mx-2">ID : </label>
      <input type="text" id="username" v-model="credentials.username">
    </div>
    <div class="mt-2">
      <label for="password" class="title-font mx-2">Password : </label>
      <input type="password" @keyup.enter="login" id="password" v-model="credentials.password">
    </div>
    <button type="button" class="btn mt-5" @click="login" :class="{ 'btn-outline-dark': isLight, 'btn-outline-light': isDark }">LOGIN</button>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Login',
  data: function () {
    return {
      credentials: {
        username: null,
        password: null,
      }
    }
  },
  methods: {
    login: function () {
      axios({
        method: 'post',
        url: 'https://ssafypedia.link/accounts/api-token-auth/',
        data: this.credentials,
      })
        .then(res => {
          console.log(res)
          localStorage.setItem('jwt', res.data.token)
          this.$store.dispatch('login')
          this.$emit('login')
          this.$router.push({ name: 'MyProfile' })
        })
        .catch(err => {
          console.log(err)
        })
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