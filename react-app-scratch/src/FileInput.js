import React from "react";

class FileInput extends React.Component {
    constructor(props) {
        super(props);
        this.handleSubmit = this.handleSubmit.bind(this);
        this.fileInput = React.createRef();
    }

    handleSubmit(event) {
        alert(`Selected file - ${this.fileInput.current.files[0].name}`);
        event.preventDefault();
    }

    render() {
        return (
            <form onSubmit={this.handleSubmit}>
                <label>
                    Name:
                    <input type="file" ref={this.fileInput} />
                </label>
                <input type="submit" value="Submit" />
            </form>
        );
    }
}

export default FileInput;
