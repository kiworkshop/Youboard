<template>
  <tr class="inputRow" v-if="data.item.rank === null || this.editMode === true">
    <td>
      <v-checkbox
          v-model="data.selected"
          primary
          hide-details
      ></v-checkbox>
    </td>
    <td class="text-xs">{{ data.item.rank }}</td>
    <td><input v-model="input.name" type="text"></td>
    <td><input v-model="input.category" type="text"></td>
    <td><input v-model="input.subscribers" type="text"></td>
    <td><input v-model="input.url" type="text"></td>

    <td class="justify-center layout px-0">
      <v-btn
          small icon depressed dark color="black"
          @click="apply()"
      >
        <v-icon>done</v-icon>
      </v-btn>
      <v-btn
          small icon depressed dark color="black"
          @click="cancel()"
      >
        <v-icon>undo</v-icon>
      </v-btn>
    </td>
  </tr>
</template>

<script>
    export default {
        name: "ChannelInputRow",
        props: {
            data: Object,
        },
        data () {
            return {
                editMode : false,
                requestUrl : 'http://localhost:5000/channel-admin',
                input: {
                    name: "",
                    category : "",
                    subscribers : "",
                    url: ""
                },
            }
        },
        created () {
            this.listenEditMode()
        },
        methods: {
            listenEditMode () {
                this.$crudEventbus.$on('editModeOn', this.pushToInput)
            },
            pushToInput (rowData) {
                if (rowData.rank === this.data.item.rank) {
                    this.editMode = true
                    Object.keys(this.input).forEach((key) => {
                        this.input[key] = rowData[key]
                    })
                }
            },
            apply () {
                let url = this.requestUrl + '/' + this.data.item.rank
                this.httpPutRequest(url, this.input, this.updateSuccess)
            },
            cancel () {
                this.editMode = false
                this.$crudEventbus.$emit('editModeOff')
            },
            updateSuccess (res) {
                this.$snackbarEventbus.$emit('showMessage', '수정되었습니다')
                this.$crudEventbus.$emit('editModeOff')
                this.editMode = false
                this.$crudEventbus.$emit('updateItem', res.data)
            }
        }
    }

</script>

<style>
    input {
        border: 1px solid lightgray;
    }
</style>
