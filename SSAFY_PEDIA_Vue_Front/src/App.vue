<template>
  <div id="app" :class="{ dark: isDark, light: isLight }">
    <nav class="navbar navbar-expand-lg sticky-top" :class="{'navbar-dark': isDark,'bg-light': isLight , 'navbar-light': isLight, 'bg-dark': isDark }">
      <div class="container-fluid" id="nav-div">
        <router-link class="navbar-brand fw-bold" :to="{ name: 'Movie' }">SSAFY PEDIA</router-link>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
          <ul class="navbar-nav me-auto mb-2 mb-lg-0">
            <li class="nav-item">
              <router-link class="nav-link fw-bold" :to="{ name: 'Movie' }">Movies</router-link>
            </li>
            <li class="nav-item">
              <router-link class="nav-link fw-bold" :to="{ name: 'Genre' }">Genre Recommend</router-link>
            </li>
            <li class="nav-item">
              <router-link class="nav-link fw-bold" :to="{ name: 'Mbti' }">Mbti Recommend</router-link>
            </li>
          </ul>
          <ul class="navbar-nav">
            <li v-if="isLogin" class="nav-item">
              <router-link class="nav-link fw-bold" :to="{ name: 'MyProfile' }">Profile</router-link>
            </li>
            <li v-if="isLogin" class="nav-item">
              <router-link class="nav-link fw-bold" @click.native="logout" to="#">Logout</router-link>
            </li>
            <li v-if="!isLogin" class="nav-item">
              <router-link class="nav-link fw-bold" :to="{ name: 'Login' }">Login</router-link>
            </li>
            <li v-if="!isLogin" class="nav-item">
              <router-link class="nav-link fw-bold" :to="{ name: 'Signup' }">Signup</router-link>
            </li>
            <li class="nav-item mousecursor" >
              <p class="nav-link fw-bold mb-0" v-if="isDark" @click="setDark">Light</p>
              <p class="nav-link fw-bold mb-0" v-if="isLight" @click="setDark">Dark</p>
            </li>
          </ul>
        </div>
      </div>
    </nav>
    <router-view @login="isLogin = true" :key="$route.fullPath"/>
  </div>
</template>
<script>

export default ({
  name: "App",
  data: function () {
    return {
      isLogin: false,
    }
  },methods: {
    logout: function () {
      this.isLogin = false
      this.$store.dispatch('logout', this.isLogin)
      localStorage.removeItem('jwt')
      this.$router.push({ name: 'Login' })
    },
    getMovies() {
      this.$store.dispatch('getMovies')
    },
    setDark: function () {
      this.$store.dispatch('setDark')
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
  created: function () {
    const token = localStorage.getItem('jwt')
    if (token) {
      this.isLogin = true
    }
  },
  mounted: function () {
    this.getMovies()
    this.$router.push({ name: "Movie" })
  },
})
</script>

<style>
 /* medium | x-small | small | large | x-large | xx-large  */
.light {
  color: #2c3e50;
}
.dark {
  background-color: rgba(0, 0, 0, 0.911);
  color: white
}
.title-font {
  font-weight: bold;
  font-size: x-large;
  text-align: left;
  margin-left: 3cm;
  margin-top: 0.5cm;
}
.content-font {
  font-weight: bold;
  font-size: large;
  text-align: left;
}
.mini-font {
  font-size: small;
  text-align: left;
}
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  height: 600vh;
}

#nav {
  padding: 30px;
  width: 100%;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}

.mousecursor {
  cursor: pointer
}
</style>
