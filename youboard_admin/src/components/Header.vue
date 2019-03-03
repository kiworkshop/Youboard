<template>
  <v-toolbar app>
    <v-toolbar-title class="title">
      <router-link to="/">
        <h3>Youboard Admin</h3>
      </router-link>
    </v-toolbar-title>

    <v-btn flat href="/channel"><span class="mr-2">channel</span></v-btn>
    <v-btn flat href="/video"><span class="mr-2">video</span></v-btn>
    <v-btn flat href="/youtuber"><span class="mr-2">youtuber</span></v-btn>
  </v-toolbar>
</template>

<script>
  export default {
    name: "Header"
  }
</script>

<style scoped>
</style>