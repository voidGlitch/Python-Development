/* eslint-disable no-unused-vars */
import React, { useContext, useState, useEffect } from "react";

import blogContext from "../context/blog/blogContext";
// import Blog from "./Blog";
import { SelectPicker } from "rsuite";
import data from "../component/data.json";

const AddBlog = () => {
  const context = useContext(blogContext);
  const { addNote } = context;
  const [blog, setBlog] = useState({
    title: "",
    description: "",
    tag: "",
    image: "",
  });
  // const [style, setStyle] = useState({ file: Adventure });
  const onclicked = (e) => {
    e.preventDefault();
    console.log(blog);
    addNote(blog.title, blog.description, blog.tag, blog.image);
  };
  const handlechange = (e) => {
    setBlog({ ...blog, [e.target.name]: e.target.value });
  };
  useEffect(() => {
    console.log(blog);
  }, []);
  const handletagchange = (value) => {
    console.log(value);
    setBlog({ ...blog, value });
    console.log(blog);
  };

  const Setimg = (value) => {
    if (value === "Adventure") {
      setBlog({ ...blog, image: data[0].image });
    }
    if (value === "Travel") {
      setBlog({ ...blog, image: data[1].image });
    }
    if (value === "Sports") {
      setBlog({ ...blog, image: data[2].image });
    }
    if (value === "Beach") {
      setBlog({ ...blog, image: data[3].image });
    }
    if (value === "Downtown") {
      setBlog({ ...blog, image: data[4].image });
    }
    if (value === "HillStation") {
      setBlog({ ...blog, image: data[5].image });
    }
    if (value === "City") {
      setBlog({ ...blog, image: data[6].image });
    }
  };
  return (
    <>
      <form className="rs-form rs-form-vertical rs-form-fixed-width ml-50">
        <div className="rs-form-group " role="group">
          <label
            id="name-control-label"
            htmlFor="title"
            className="rs-form-control-label"
          >
            Title
          </label>

          <div className="rs-form-control rs-form-control-wrapper">
            <input
              aria-labelledby="name-control-label"
              aria-describedby="name-help-text"
              name="title"
              className="rs-input"
              type="text"
              id="title"
              onChange={handlechange}
            />
          </div>

          <span id="name-help-text" className="rs-form-help-text">
            Title is required
          </span>
        </div>
        <div className="rs-form-group" role="group">
          <label htmlFor="description" className="rs-form-control-label">
            Description
          </label>
          <div className="rs-form-control rs-form-control-wrapper">
            <textarea
              aria-labelledby="email-control-label"
              aria-describedby="email-help-text"
              name="description"
              className="rs-input"
              type="textarea"
              id="description"
              style={{ width: "500px", height: "150px" }}
              onChange={handlechange}
            />
            <span id="name-help-text" className="rs-form-help-text">
              Description is required
            </span>
          </div>
        </div>

        <div className="mt-3">
          <span className="mt-1">Tag</span>
          <br></br>
          <SelectPicker
            data={data}
            // defaultValue={2}
            valueKey="value"
            labelKey="label"
            style={{ width: 500 }}
            onChange={(value) => {
              console.log(value);
              handletagchange(value);
              Setimg(value);
            }}
          />
        </div>

        <div className="rs-form-group mt-3" role="group">
          <div role="toolbar" className="rs-btn-toolbar">
            <button
              type="button"
              className="rs-btn rs-btn-primary"
              onClick={onclicked}
            >
              Submit
              <span className="rs-ripple-pond">
                <span className="rs-ripple"></span>
              </span>
            </button>
            <button type="button" className="rs-btn rs-btn-default">
              Cancel
              <span className="rs-ripple-pond">
                <span className="rs-ripple"></span>
              </span>
            </button>
          </div>
        </div>
      </form>
    </>
  );
};

export default AddBlog;
