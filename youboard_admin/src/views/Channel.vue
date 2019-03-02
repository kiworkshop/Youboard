<template>
    <v-container fluid grid-list-xs>
        <v-layout row wrap>
            <v-flex xs12 offset-xs1>
                <h3>Channel 관리 page</h3>
            </v-flex>
            <v-flex xs12>
                <v-data-table
                    :headers="tableHeader"
                    :items="list"
                    v-model="selectedRows"
                    item-key="id"
                    select-all
                >
                    <template slot="items" slot-scope="channels">
                        <ChannelInputRow :data="channels"></ChannelInputRow>
                        <ChannelRow :data="channels"></ChannelRow>
                    </template>
                </v-data-table>
            </v-flex>
        </v-layout>
    </v-container>
</template>

<script>
    import { axiosMixin } from '@/components/mixins/axiosMixin'
    import ChannelRow from '@/components/channel/ChannelRow'
    import ChannelInputRow from '@/components/channel/ChannelInputRow'

    export default {
        name: "Channel",
        components: {
            ChannelRow,
            ChannelInputRow,
        },
        mixins: [axiosMixin],
        data () {
            return {
                url : 'http://localhost:5000/channel-admin',
                tableHeader : [
                    { text: "Rank", value: "rank", align: "center" },
                    { text: "name", value: "name", align: "center" },
                    { text: "category", value: "category", align: "center" },
                    { text: "subscribers", value: "subscribers", align: "center" },
                    { text: "url", value: "url" },
                    { text: "action", value: "id" },
                ],
                selectedRows: [],
                list : [],
            }
        },
        created () {
            this.fetchList()
        },
        methods: {
            fetchList() {
                this.httpGetRequest(this.url, this.pushList)
            },
            pushList (res) {
                this.list = res.data
            }
        }
    }
</script>