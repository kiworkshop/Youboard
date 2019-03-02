export const axiosMixin = {
    methods: {
        httpGetRequest(url, callback) {
            this.$http.get(url)
            .then(res => {
                if (callback) {
                    callback(res);
                }
            })
            .catch((error) => {
                // TODO: add snackbar, etc.
            })
        }
    }
}