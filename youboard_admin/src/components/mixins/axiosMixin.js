export const axiosMixin = {
    methods: {
        httpGetRequest(url, callback) {
            this.$http.get(url)
            .then(res => {
                if (callback) {
                    callback(res);
                }
            })
            .catch(() => {
                this.$snackbarEventbus.$emit('showMessage', '데이터를 불러올 수 없습니다')
            })
        },
        httpPutRequest(url, requestForm, callback) {
            this.$http.put(url, requestForm)
            .then(res => {
                if (callback) {
                    callback(res);
                }
            })
            .catch((error) => {
                this.$snackbarEventbus.$emit('showMessage', error.response.status + '수정 실패')
            })
        },
        httpDeleteRequest(url, callback) {
            this.$http.delete(url)
            .then(res => {
                if (callback) {
                    callback(res);
                }
            })
            .catch((error) => {
                this.$snackbarEventbus.$emit('showMessage', error.response.status + '삭제 실패')
            })
        }
    }
}