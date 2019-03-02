<template>
  <v-snackbar
      v-model="show"
      :bottom="true"
      :right="true"
      :timeout="3000"
  >
    {{ message }}
    <v-btn color="primary" flat @click="show = false">
      Close
    </v-btn>
  </v-snackbar>
</template>

<script>
  export default {
    name: "Snackbar",
    data () {
      return {
        show: false,
        message: ''
      }
    },
    created () {
      this.$snackbarEventBus.$on('showMessage', (message) => {
        this.message = message
        this.show = true
      })
    }
  }
</script>

<style scoped>

</style>